from flask import jsonify, Flask, request
from models import db, Ticket
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

@app.route("/Ticket", methods=["POST"])
def register_ticket():
    code = request.args.get('code')
    if not code:
        return jsonify({"error": "Code is required"}), 400
    if len(code) != 12:
        return jsonify({"error": "Code must be 12 characters long"}), 400
    
    new_ticket = Ticket(code=code)
    db.session.add(new_ticket)
    db.session.commit()
    
    return jsonify(
        {"code": new_ticket.code,
         "valid": "Y"}
    ), 201
    
@app.route("/Ticket/<code>", methods=["POST"])
def check_ticket(code):
    ticket = Ticket.query.filter_by(code=code).first()
    
    if not ticket:
        return jsonify({"error": "Tiket not found"}), 404
    
    if ticket.valid == "N":
        return jsonify({"error": "Ticket is invalid"}), 200
    
    ticket.valid = "N"
    db.session.commit()
    return jsonify({"message": "Ticket is valid"}), 200

@app.route("/Tickets/valid", methods=["GET"])
def get_valid_tickets():
    tickets = Ticket.query.filter_by(valid="Y").all()
    if not tickets:
        return jsonify([{"error": "No valid tickets found"}]), 404   #can be also 200 returning an empty list
    result = []
    for t in tickets:
        result.append({
            "code": t.code,
            "valid": t.valid
        })
    return jsonify(result), 200

if __name__ == "__main__":
    app.run(debug=True)