from flask import Blueprint, send_from_directory, g

bp = Blueprint('stream', __name__, url_prefix='/stream')


@bp.route('/<path:filename>', methods=('GET',))
def download_file(filename):
    print(filename)
    return send_from_directory('/home/guibos/PycharmProjects/toriiserver-v2/data',
                               filename, as_attachment=True)