from flask import request
from flask import Blueprint
# from .model.models import author_bp
from flaskApp.model.models import Author
author_bp = Blueprint('author', __name__)



@author_bp.route('/author/new')
def new_author():
    """Creates a new author by a giving name (via GET parameter)
    e.g.: GET /author/new?name=Francisco creates a author named Francisco
    """
    print "00000000009090"
    print author_bp
    author = Author(name=request.args.get('name', ''))
    author.save()
    return 'Saved :)'

@author_bp.route('/authors/')
def list_authors():
   """List all authors.
   e.g.: GET /authors"""
   authors = Author.query.all()
   content = '<p>Authors:</p>'
   for author in authors:
       content += '<p>%s</p>' % author.name
   return content


@author_bp.route('/message/',method=['get'])
def message():
    return "message"