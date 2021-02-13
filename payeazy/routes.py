import json
from flask import request, jsonify, g
from payeazy.models import CurrentProjects, Transaction, Employer, Freelancer, db
from payeazy import app
import datetime
from datetime import timedelta
from block import getAccountBalance, callconstructor, transferMoneyToFreelancer, addFreelancerToContract, transferMoneyToFamilyMember

# Frontend Routes


@app.route('/', methods=["GET", "POST"])
def catch():
    return app.send_static_file('index.html')


# Backend Routes

@app.route('/backend/empprofile', methods=["POST"])
def employer_profile():
    content = request.get_json()
    name = content["name"]
    email = content["email"]
    address = content["address"]
    password = content["password"]

    emp = Employer(name=name, email=email, address=address, password=password)

    db.session.add(emp)
    db.session.commit()

    return 'New employer added', 200


@app.route('/backend/freeprofile', methods=["POST"])
def freelancer_profile():
    content = request.get_json()
    name = content["name"]
    email = content["email"]
    address = content["address"]
    password = content["password"]

    free = Freelancer(name=name, email=email,
                      address=address, password=password)

    db.session.add(free)
    db.session.commit()

    return 'New freelancer added', 200


@app.route('/backend/freelogin', methods=["POST", "GET"])
def freelancer_login():
    content = request.get_json()
    email = content["email"]
    password = content["password"]

    free = Freelancer.query.filter(Freelancer.email == email, Freelancer.password == password)
    if not free:
        return 'Invalid Credential', 400

    address = free.address
    current_balance = getAccountBalance(address)


    List = []
    Dict = {
        'name': free.name,
        'current_balance': current_balance
    }
    List.append(Dict)

    return json.dumps(List)


@app.route('/backend/emplogin', methods=["POST", "GET"])
def employer_login():
    content = request.get_json()
    email = content["email"]
    password = content["password"]

    emp = Employer.query.filter(
        Employer.email == email, Employer.password == password)
    if not emp:
        return 'Invalid Credential', 400

    address = emp.address
    current_balance = getAccountBalance(address)

    List = []
    Dict = {
        'name': emp.name,
        'current_balance': current_balance
    }
    List.append(Dict)

    return json.dumps(List)


@app.route('/backend/freeworking', methods=["GET", "POST"])
def freelancer_working():
    content = request.get_json()
    emp_email = content["emp_email"]

    emp = Employer.query.filter(Employer.email == emp_email).first()
    emp_address = emp.address

    rows = CurrentProjects.query.filter(
        CurrentProjects.emp_email == emp_email).all()

    List = []
    Dict = {}

    for row in rows:
        Dict = {
            'sno': row.sno,
            'free_name': row.free_name,
            'free_email': row.free_email,
            'project': row.project,
            'date_started': row.date_started,
            'deadline': row.deadline,
            'days_hours_work': row.days_hours_work,
            'rate_day_hour': row.rate_day_hour,
            'proposed_amount': row.proposed_amount
        }
        List.append(Dict)

    return json.dumps(List)


@app.route('/backend/freepayment', methods=["GET", "POST"])
def freelancer_payment():
    try:
        content = request.get_json()
        sno = content["sno"]
        no_of_leaves = content["no_of_leaves"]
        rate_for_leave_deduct = content["rate_for_leave_deduct"]
        amount_paid = content["amount_paid"]
        private_key = content["private_key"]

        row = CurrentProjects.query.filter(CurrentProjects.sno == sno).first()

        callconstructor(row.rate_day_hour, row.days_hours_work,
                        rate_for_leave_deduct)

        hex_tr = transferMoneyToFreelancer(
            row.emp_address, row.free_address, private_key, no_of_leaves)

        Dict = {'hex': hex_tr}
        List = []
        List.append(Dict)

        transact = Transaction(emp_name=row.emp_name, emp_email=row.emp_email,
                               free_name=row.free_name, free_email=row.free_email,
                               project=row.project, date_started=row.date_started, deadline=row.deadline,
                               days_hours_work=row.no_days_hours, rate_day_hour=row.rate_day_hour,
                               proposed_amount=row.proposed_amount, no_of_leaves=no_of_leaves,
                               rate_for_leave_deduct=rate_for_leave_deduct, amount_paid=amount_paid,
                               emp_address=row.emp_address, free_address=row.free_address)

        db.session.add(transact)
        db.session.commit()

        db.session.delete(row)
        db.session.commit()

        return json.dumps(List)

    except:
        return 'Payment Unsuccessful', 400


@app.route('/backend/addproject', methods=["POST", "GET"])
def add_project():
    content = request.get_json()
    emp_name = content["emp_name"]
    emp_email = content["emp_email"]
    free_name = content["free_name"]
    free_email = content["free_email"]
    project = content["project"]
    date_started = content["date_started"]
    deadline = content["deadline"]
    no_days_hours = content["days_hours_work"]
    rate_day_hour = content["rate_day_work"]
    proposed_amount = content["proposed_amount"]
    free_address = content["free_address"]

    freelancer = Freelancer.query.filter(
        Freelancer.email == free_email).first()

    if(freelancer.address != free_address):
        return 'Freelancer Address Invalid', 400

    emp = Employer.query.filter(Employer.email == emp_email).first()
    emp_address = emp.address

    proj = CurrentProjects(emp_name=emp_name, emp_email=emp_email,
                           free_name=free_name, free_email=free_email,
                           project=project, date_started=date_started, deadline=deadline,
                           days_hours_work=no_days_hours, rate_day_hour=rate_day_hour,
                           proposed_amount=proposed_amount, emp_address=emp_address, free_address=free_address)

    db.session.add(proj)
    db.session.commit()

    return 'New project added', 200


@app.route('/backend/employerhistory', methods=["GET"])
def employerhistory():
    content = request.get_json()
    email = content["emp_email"]

    rows = Transaction.query.filter(Transaction.emp_email == email).all()

    List = []
    Dict = {}

    for row in rows:
        Dict = {
            'free_name': row.free_name,
            'free_email': row.free_email,
            'project': row.project,
            'date_started': row.date_started,
            'deadline': row.deadline,
            'days_hours_work': row.days_hours_work,
            'rate_day_hour': row.rate_day_hour,
            'proposed_amount': row.proposed_amount,
            'no_of_leaves': row.no_of_leaves,
            'rate_for_leave_deduct': row.rate_for_leave_deduct,
            'amount_paid': row.amount_paid,
            'free_address': row.free_address
        }
        List.append(Dict)

    return json.dumps(List)


@app.route('/backend/freelancerhistory', methods=["GET"])
def freelancerhistory():
    content = request.get_json()
    email = content["free_email"]

    rows = Transaction.query.filter(Transaction.free_email == email).all()

    List = []
    Dict = {}

    for row in rows:
        Dict = {
            'emp_name': row.emp_name,
            'emp_email': row.emp_email,
            'project': row.project,
            'date_started': row.date_started,
            'deadline': row.deadline,
            'days_hours_work': row.days_hours_work,
            'rate_day_hour': row.rate_day_hour,
            'proposed_amount': row.proposed_amount,
            'no_of_leaves': row.no_of_leaves,
            'rate_for_leave_deduct': row.rate_for_leave_deduct,
            'amount_paid': row.amount_paid,
            'emp_address': row.emp_address
        }
        List.append(Dict)

    return json.dumps(List)


@app.route('/backend/projectworking', methods=["GET", "POST"])
def project_working():
    content = request.get_json()
    free_email = content["free_email"]

    rows = CurrentProjects.query.filter(
        CurrentProjects.free_email == free_email).all()

    List = []
    Dict = {}

    for row in rows:
        Dict = {
            'sno': row.sno,
            'emp_name': row.emp_name,
            'emp_email': row.emp_email,
            'project': row.project,
            'date_started': row.date_started,
            'deadline': row.deadline,
            'days_hours_work': row.days_hours_work,
            'rate_day_hour': row.rate_day_hour,
            'proposed_amount': row.proposed_amount
        }
        List.append(Dict)

    return json.dumps(List)


@app.route('/backend/transfer', methods=["GET"])
def transfer():
    try:
        content = request.get_json()
        name = content["name"]
        email = content["email"]
        amount = content["amount"]
        address = content["address"]
        private_key = content["private_key"]
        free_email = content["free_email"]

        free = Freelancer.query.filter(Freelancer.email == free_email).first()
        free_address = free.address

        hex_tr = transferMoneyToFamilyMember(
            free_address, address, private_key, amount)

        Dict = {'hex': hex_tr}
        List = []
        List.append(Dict)

        return json.dumps(List)
    except:
        return 'Payment Unsuccessful', 400
