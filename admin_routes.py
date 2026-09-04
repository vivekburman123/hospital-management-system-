# routes/admin_routes.py
from flask import Blueprint, request, jsonify
from models.doctor import Doctor
from app import db

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/doctor', methods=['GET'])
def add_doctor():
    data = request.get_json()
    doctor = Doctor(**data)
    db.session.add(doctor)
    db.session.commit()
    return jsonify({'msg': 'Doctor added'}), 201

@admin_bp.route('/doctors', methods=['GET'])
def get_doctors():
    doctors = Doctor.query.all()
    return jsonify([{'id': d.id, 'name': d.name, 'specialization': d.specialization} for d in doctors])

