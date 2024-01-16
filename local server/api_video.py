from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
api = Api(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)
token = "test1234"


class VideoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    views = db.Column(db.Integer, nullable=False)
    likes = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Video(name = {self.name}, views = {self.views}, Likes = {self.likes})"


video_put_args = reqparse.RequestParser()
video_put_args.add_argument('name', type=str, required=True, help='Name of the video')
video_put_args.add_argument('views', type=int, required=True, help="views of the video")
video_put_args.add_argument("likes", type=int, required=True, help="likes on a video")

video_update_args = reqparse.RequestParser()
video_update_args.add_argument('name', type=str, help='Name of the video')
video_update_args.add_argument('views', type=int, help="views of the video")
video_update_args.add_argument("likes", type=int, help="likes on a video")

resourse_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'views': fields.Integer,
    'likes': fields.Integer
}



class Video(Resource):

    @marshal_with(resourse_fields)
    def get(self, video_id):
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404, message="No video with that ID found.")
        return result

    @marshal_with(resourse_fields)
    def put(self, video_id):
        args = video_put_args.parse_args()
        result = VideoModel.query.filter_by(id=video_id).first()
        if result:
            abort(409, message="Video id taken..")

        video = VideoModel(id=video_id, name=args['name'], views=args['views'], likes=args['likes'])
        db.session.add(video)
        db.session.commit()
        return video, 201


    @marshal_with(resourse_fields)
    def patch(self, video_id):
        args = video_update_args.parse_args()
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404, message="Video doesn't exist, cannot update")

        if args["name"]:
            result.name = args["name"]
        if args["views"]:
            result.views = args["views"]
        if args["likes"]:
            result.likes = args["likes"]

        db.session.commit()

        return result  # Add this line to return the updated video


    @marshal_with(resourse_fields)
    def delete(self, video_id):  # Add the video_id parameter
        pass

api.add_resource(Video,"/video/<int:video_id>")


if __name__ == "__main__":
    app.run(debug=True)