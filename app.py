from flask import Flask,request,jsonify

app = Flask(__name__)

def check_appointment_availability(start_time,end_time):
    if start_time>=4 and end_time<=6:
        return False
    
    if start_time>end_time:
        return False

    if start_time==0 or end_time==0:
        return False

    if end_time>10:
        return False

    return True


@app.route("/")
def home():
    return "Welcome to Clinic appointment system"

@app.route("/check_appointment", methods=["POST"])
def check_appointment():
    data=request.get_json()
    start_time=data["start_time"]
    end_time=data["end_time"]

    if check_appointment_availability(start_time,end_time):
        return jsonify({"message":"Appointment booked"}),200

    return jsonify({"message":"Appointment slot not available or booked already"}),400


if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000)


