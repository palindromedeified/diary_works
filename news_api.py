import flask

from data import db_session
from data.jobs import Jobs

bluprint = flask.Blueprint('jobs_api', __name__, template_folder='templates')


@bluprint.route('/api/jobs')
def get_jobs():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    return flask.jsonify({
        'jobs': [item.to_dict(
            only=('id', 'job', 'team_leader', 'work_size', 'collaborators', 'start_date', 'end_date',
                  'is_finished', 'category')
        ) for item in jobs]
    })
