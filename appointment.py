# models/appointment.py
from app import db

class Appointment(db.Model):
     __tablename__ = 'appointment'
     id = db.Column(db.Integer, primary_key=True)
     patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'), nullable=False)
     doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.id'), nullable=False)
     date = db.Column(db.DateTime, nullable=False)
     description = db.Column(db.Text)
