from pyramid.view import view_config
from pyramid.config import Configurator
from pyramid.response import FileResponse

def test_page(request):
  response = FileResponse(
      '/home/sharefoxy/lsbaws/part2/images/png19.png',
      request=request,
      content_type='image/png'
      )
  return response


config = Configurator()
config.add_route('png', '/png19.png')
config.add_view(test_page, route_name='png')
app = config.make_wsgi_app()
