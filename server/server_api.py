from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
api = Api(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///challange.db"
db = SQLAlchemy(app)


class Kluis(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String, nullable=False, unique=True)
    adres_id = db.Column(db.Integer, nullable=False)
    gebruiker_id = db.Column(db.Integer, nullable=False)
    status = db.Column(db.Integer, nullable=False)
    pakket_id = db.Column(db.Integer, nullable=False)

    
    def __repr__(self) -> str:
        return f"Kluis(id = {self.id}, code = {self.code}, adres_id = {self.adres_id}, gebruiker_id = {self.gebruiker_id}, status = {self.status}, pakket_id = {self.pakket_id})"

class Kluis_adres(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    kluis_id = db.Column(db.Integer, nullable=False)
    postcode = db.Column(db.String, nullable=False)
    street = db.Column(db.String, nullable=False)
    huisnummer = db.Column(db.String, nullable=False)

    def __repr__(self) -> str:
        return f"Kluis_adres(id = {self.id}, kluis_id = {self.kluis_id}, postcode = {self.postcode}, straat = {self.street}, huisnummer = {self.huisnummer})"
    
    
class Gebruiker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String,unique=True, nullable=False)
    telefoon = db.Column(db.String, unique=True, nullable=False)

    def __repr__(self) -> str:
        return f"Gebruiker(id = {self.id}, username = {self.username}, )"
    
class Pakket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    naam = db.Column(db.String, nullable=False)
    inhoud = db.Column(db.String, nullable=False)
    houdbaarheid = db.Column(db.String, nullable=False)

    def __repr__(self) -> str:
        return f"Pakket(id = {self.id}, naam = {self.naam}, inhoud = {self.inhoud}, houdbaarheid = {self.houdbaarheid})"

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    admin = db.Column(db.Boolean, default=False)
    def __repr__(self) -> str:
        return f"Users(id = {self.id}, name = {self.name}, password = {self.password}, admin = {self.admin})"

app.app_context().push()
db.create_all()

users_put_args = reqparse.RequestParser()
users_put_args.add_argument('name', type=str, required=True, help='No user name provided')
users_put_args.add_argument('password', type=str, required=True, help='No password provided')
users_put_args.add_argument('admin', type=bool, required=True, help='No admin status provided')

users_update_args = reqparse.RequestParser()
users_update_args.add_argument('name', type=str, required=True, help='No user name provided')
users_update_args.add_argument('password', type=str, required=True, help='No password provided')
users_update_args.add_argument('admin', type=bool, required=True, help='No admin status provided')



kluis_put_args = reqparse.RequestParser()
kluis_put_args.add_argument('code', type=str, required=True, help="Code of the kluis")
kluis_put_args.add_argument("adres_id", type=int, required=True, help="Adress ID")
kluis_put_args.add_argument("gebruiker_id", type=int, required=True, help="Gebruiker ID")
kluis_put_args.add_argument("status", type=str, required=True, help="status of the kluis")
kluis_put_args.add_argument("pakket_id", type=int, required=True, help="pakket ID")

kluis_update_args = reqparse.RequestParser()
kluis_update_args.add_argument('code', type=str, help="Code of the kluis")
kluis_update_args.add_argument("adres_id", type=int, help="Adress ID")
kluis_update_args.add_argument("gebruiker_id", type=int, help="Gebruiker ID")
kluis_update_args.add_argument("status", type=str, help="status of the kluis")
kluis_update_args.add_argument("pakket_id", type=int, help="pakket ID")

kluis_adres_put_args = reqparse.RequestParser()
kluis_adres_put_args.add_argument('kluis_id', type=str, required=True, help='ID of the kluis')
kluis_adres_put_args.add_argument('postcode', type=str, required=True, help='postcode of the kluis')
kluis_adres_put_args.add_argument('street', type=str, required=True, help='straat of the kluis')
kluis_adres_put_args.add_argument('huisnummer', type=str, required=True, help='huisnummer of the kluis')

kluis_adres_update_args = reqparse.RequestParser()
kluis_adres_update_args.add_argument('kluis_id', type=str, help='ID of the kluis')
kluis_adres_update_args.add_argument('postcode', type=str, help='postcode of the kluis')
kluis_adres_update_args.add_argument('street', type=str, help='straat of the kluis')
kluis_adres_update_args.add_argument('huisnummer', type=str, help='huisnummer of the kluis')

gebruker_put_args = reqparse.RequestParser()
gebruker_put_args.add_argument('username', type=str, required=True, help='Name of the user')
gebruker_put_args.add_argument('email', type=str, required=True, help='Email of the user')
gebruker_put_args.add_argument('telefoon', type=str, required=True, help='Telefoon of the user')

gebruker_update_args = reqparse.RequestParser()
gebruker_update_args.add_argument('username', type=str, help='Name of the user')
gebruker_update_args.add_argument('email', type=str, help='Email of the user')
gebruker_update_args.add_argument('telefoon', type=str, help='Telefoon of the user')

pakket_put_args = reqparse.RequestParser()
pakket_put_args.add_argument('naam', type=str, required=True, help='Naam van het pakket')
pakket_put_args.add_argument('inhoud', type=str, required=True, help='inhoud van het pakket')
pakket_put_args.add_argument('houdbaarheid', type=str, required=True, help='Houdbaarheid van het pakket')

pakket_update_args = reqparse.RequestParser()
pakket_update_args.add_argument('naam', type=str, help='Naam van het pakket')
pakket_update_args.add_argument('inhoud', type=str, help='inhoud van het pakket')
pakket_update_args.add_argument('houdbaarheid', type=str, help='Houdbaarheid van het pakket')

resourse_field_users = {
    'id': fields.Integer,
    'name': fields.String,
    'password': fields.String,
    'admin': fields.Boolean
}


resourse_fields_kluis = {
    'id': fields.Integer,
    'code': fields.String,
    'adres_id': fields.Integer,
    'gebruiker_id': fields.Integer,
    'status': fields.Integer,
    'pakket_id': fields.Integer
}

resourse_fields_kluis_adres = {
    'id': fields.Integer,
    'kluis_id': fields.Integer,
    'postcode': fields.String,
    'street': fields.String,
    'huisnummer': fields.String
}
resource_fields_gebruiker = {
    'id': fields.Integer,
    'username': fields.String,
    'email': fields.String,
    'telefoon': fields.String
}
resource_fields_pakket = {
    'id': fields.Integer,
    'naam': fields.String,
    'inhoud': fields.String,
    'houdbaarheid': fields.String
}

class Users_api(Resource):

    @marshal_with(resourse_field_users)
    def get(self,user_id):
        result = Users.query.filter_by(id=user_id).first()
        if not result:
            abort(404, message="geen user kut")
        return result
    
    @marshal_with(resourse_field_users)
    def put(self,user_id):
        args = users_put_args.parse_args()
        result = Users.query.filter_by(id=user_id).first()
        if result:
            abort(409, message="User bestaat al kut")

        user = Users(id=user_id, name=args["name"],password=args["password"],admin=args["admin"])
        db.session.add(user)
        db.session.commit()
        return user, 201
        
    
    @marshal_with(resourse_field_users)
    def patch(self,user_id):
        args = users_update_args.parse_args()
        result = Users.query.filter_by(id=user_id).first()
        if not result:
            abort(404, message="geen user kut, kan nie verandere he")

        if args["id"]:
            result.id = args["id"]
        if args["name"]:
            result.name = args["name"]
        if args["password"]:
            result.password = args["password"]
        if args["admin"]:
            result.admin = args["admin"]
        
        db.session.commit()

        return result
    
    @marshal_with(resourse_field_users)
    def delete(self,user_id):
        result = Users.query.filter_by(id=user_id).first()
        if not result:
            abort(404, message="geen users kut")
        db.session.delete(result)
        db.session.commit()
        return result, 200
    


class Kluis_api(Resource):

    @marshal_with(resourse_fields_kluis)
    def get(self,kluis_id):
        result = Kluis.query.filter_by(id=kluis_id).first()
        if not result:
            abort(404, message="geen kluis kut")
        return result
    
    @marshal_with(resourse_fields_kluis)
    def put(self,kluis_id):
        args = kluis_put_args.parse_args()
        result = Kluis.query.filter_by(id=kluis_id).first()
        if result:
            abort(409, message="Kluis bestaat al kut")

        kluis = Kluis(id=kluis_id, code=args["code"], 
                     adres_id=args["adres_id"], gebruiker_id=args["gebruiker_id"],
                     status=args["status"], pakket_id=args["pakket_id"])
        db.session.add(kluis)
        db.session.commit()
        return kluis, 201
        
    
    @marshal_with(resourse_fields_kluis)
    def patch(self,kluis_id):
        args = kluis_update_args.parse_args()
        result = Kluis.query.filter_by(id=kluis_id).first()
        if not result:
            abort(404, message="geen kluis kut, kan nie verandere he")

        if args["code"]:
            result.code = args["code"]
        if args["adres_id"]:
            result.adres_id = args["adres_id"]
        if args["gebruiker_id"]:
            result.gebruiker_id = args["gebruiker_id"]
        if args["status"]:
            result.status = args["status"]
        if args["pakket_id"]:
            result.pakket_id = args["pakket_id"]
        
        db.session.commit()

        return result
    
    @marshal_with(resourse_fields_kluis)
    def delete(self,kluis_id):
        result = Kluis.query.filter_by(id=kluis_id).first()
        if not result:
            abort(404, message="geen kluis kut")
        db.session.delete(result)
        db.session.commit()
        return result, 200
    
class Kluis_adres_api(Resource):

    @marshal_with(resourse_fields_kluis_adres)
    def get(self,kluis_adres_id):
        result = Kluis_adres.query.filter_by(id=kluis_adres_id).first()
        if not result:
            abort(404, message="geen kluis_adres kut")
        return result
    
    @marshal_with(resourse_fields_kluis_adres)
    def put(self,kluis_adres_id):
        args = kluis_adres_put_args.parse_args()
        result = Kluis_adres.query.filter_by(id=kluis_adres_id).first()
        if result:
            abort(409, message="Kluis bestaat al kut")

        kluis_adres = Kluis_adres(id=kluis_adres_id, kluis_id=args["kluis_id"], 
                            postcode=args["postcode"], street=args["street"],
                            huisnummer=args["huisnummer"])
        db.session.add(kluis_adres)
        db.session.commit()
        return kluis_adres, 201
        
    
    @marshal_with(resourse_fields_kluis_adres)
    def patch(self,kluis_adres_id):
        args = kluis_adres_update_args.parse_args()
        result = Kluis_adres.query.filter_by(id=kluis_adres_id).first()
        if not result:
            abort(404, message="geen kluis_adres kut, kan nie verandere he")

        if args["kluis_id"]:
            result.kluis_id = args["kluis_id"]
        if args["postcode"]:
            result.postcode = args["postcode"]
        if args["street"]:
            result.street = args["street"]
        if args["huisnummer"]:
            result.huisnummer = args["huisnummer"]
        
        db.session.commit()

        return result
    
    @marshal_with(resourse_fields_kluis_adres)
    def delete(self,kluis_adres_id):
        result = Kluis_adres.query.filter_by(id=kluis_adres_id).first()
        if not result:
            abort(404, message="geen kluis_adres kut")
        db.session.delete(result)
        db.session.commit()
        return result, 200

class Gebruiker_api(Resource):

    @marshal_with(resource_fields_gebruiker)
    def get(self,gebruiker_id):
        result = Gebruiker.query.filter_by(id=gebruiker_id).first()
        if not result:
            abort(404, message="geen gebruiker kut")
        return result
    
    @marshal_with(resource_fields_gebruiker)
    def put(self,gebruiker_id):
        args = gebruker_put_args.parse_args()
        result = Gebruiker.query.filter_by(id=gebruiker_id).first()
        if result:
            abort(409, message="gebruiker bestaat al kut")

        gebruiker = Gebruiker(id=gebruiker_id, username=args["username"], 
                            email=args["email"], telefoon=args["telefoon"])
        db.session.add(gebruiker)
        db.session.commit()
        return gebruiker, 201
        
    
    @marshal_with(resource_fields_gebruiker)
    def patch(self,gebruiker_id):
        args = gebruker_update_args.parse_args()
        result = Gebruiker.query.filter_by(id=gebruiker_id).first()
        if not result:
            abort(404, message="geen gebruiker kut, kan nie verandere he")

        if args["id"]:
            result.id = args["id"]
        if args["username"]:
            result.username = args["username"]
        if args["email"]:
            result.email = args["email"]
        if args["telefoon"]:
            result.telefoon = args["telefoon"]
        
        db.session.commit()

        return result
    
    @marshal_with(resource_fields_gebruiker)
    def delete(self,gebruiker_id):
        result = Gebruiker.query.filter_by(id=gebruiker_id).first()
        if not result:
            abort(404, message="geen gebruiker kut")
        db.session.delete(result)
        db.session.commit()
        return result, 200

class Pakket_api(Resource):

    @marshal_with(resource_fields_pakket)
    def get(self,pakket_id):
        result = Pakket.query.filter_by(id=pakket_id).first()
        if not result:
            abort(404, message="geen pakket kut")
        return result
    
    @marshal_with(resource_fields_pakket)
    def put(self,pakket_id):
        args = pakket_put_args.parse_args()
        result = Pakket.query.filter_by(id=pakket_id).first()
        if result:
            abort(409, message="pakket bestaat al kut")

        pakket = Pakket(id=pakket_id, naam=args["naam"], 
                            inhoud=args["inhoud"], houdbaarheid=args["houdbaarheid"])
        db.session.add(pakket)
        db.session.commit()
        return pakket, 201
        
    
    @marshal_with(resource_fields_pakket)
    def patch(self,pakket_id):
        args = pakket_update_args.parse_args()
        result = Pakket.query.filter_by(id=pakket_id).first()
        if not result:
            abort(404, message="geen pakket kut, kan nie verandere he")

        if args["id"]:
            result.id = args["id"]
        if args["naam"]:
            result.naam = args["naam"]
        if args["inhoud"]:
            result.inhoud = args["inhoud"]
        if args["houdbaarheid"]:
            result.houdbaarheid = args["houdbaarheid"]
        
        db.session.commit()

        return result
    
    @marshal_with(resource_fields_pakket)
    def delete(self,pakket_id):
        result = Pakket.query.filter_by(id=pakket_id).first()
        if not result:
            abort(404, message="geen pakket kut")
        db.session.delete(result)
        db.session.commit()
        return result, 200

api.add_resource(Users_api,"/Paard/<int:user_id>")
api.add_resource(Kluis_api,"/kluis/<int:kluis_id>")
api.add_resource(Kluis_adres_api,"/kluis_adres/<int:kluis_adres_id>")
api.add_resource(Gebruiker_api,"/gebruiker/<int:gebruiker_id>")
api.add_resource(Pakket_api,"/pakket/<int:pakket_id>")


if __name__ == "__main__":
    with app.app_context():
        app.run(debug=True)
    