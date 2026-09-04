# routes/patient_routes.pyfrom flask import Blueprint, request, jsonify
from flask import Blueprint, request, jsonify, render_template
from models.patient import Patient
from models.appointment import Appointment
from app import db

patient_bp = Blueprint('patient', __name__)

# ✅ HTML page render
@patient_bp.route('/book', methods=['GET'])
def show_book_page():
    return render_template('book_appointment.html')

# ✅ JSON post request handle
@patient_bp.route('/book', methods=['POST'])
def book_appointment():
    if not request.is_json:
        return jsonify({"error": "Content-Type must be application/json"}), 415

    data = request.get_json()

    try:
        appointment = Appointment(**data)
        db.session.add(appointment)
        db.session.commit()
        return jsonify({'msg': 'Appointment booked'}), 201
    except Exception as e:
        db.session.rollback()  
        return jsonify({'error': str(e)}), 400


