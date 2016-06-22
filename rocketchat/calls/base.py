import logging
import pprint
import requests


logger = logging.getLogger(__name__)


class RocketChatBase(object):
    settings = None
    endpoint = None
    headers = None
    method = 'get'

    def __init__(self, settings=None, *args, **kwargs):
        self.settings = settings

    def post_response(self, result):
        return result

    def build_endpoint(self, **kwargs):
        """
        Build the endpoint for the user given some **kwargs
        from the initial calling.
        :return:
        """

        raise NotImplementedError()

    def build_payload(self, **kwargs):
        """
        Build a payload dict that will be passed directly to the
        endpoint.  If you need to pass this as plain text or whatever
        you'll need to the dumping here.

        :return:
        """

        return None

    def call(self, *args, **kwargs):
        """

        :param args:
        :param kwargs:
        :return:
        """

        timeout = kwargs.get('timeout', None)


        result = requests.request(method=self.method, url=self.build_endpoint(**kwargs),
                                  data=self.build_payload(**kwargs),
                                  headers=self.headers, timeout=timeout)

        request_data = {
            'url': self.build_endpoint(**kwargs),
            'method': self.method,
            'payload': self.build_payload(**kwargs),
            'headers': self.headers,
        }

        logger.debug('API Request - {request}'.format(
            request=pprint.pformat(request_data)
        ))

        result.raise_for_status()

        try:
            logger.debug('API Response - {data}'.format(
                data=pprint.pformat(result.json())
            ))
            return self.post_response(result.json())

        except Exception as e:
            logger.error('RESTful {classname} call failed. {message}'.format(
                classname=self.__class__.__name__, message=e),
                exc_info=True)
            raise e


class RESTfulPostBase(RocketChatBase):
    method = 'post'

