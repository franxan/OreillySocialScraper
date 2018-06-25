from core import init
import argparse


def main():
    # define arguments
    parser = argparse.ArgumentParser(
        description="o'Reilly Author Social Inspector"
    )
    parser.add_argument('-s',
                        '--server',
                        type=str,
                        default='127.0.0.1',
                        required=False)
    parser.add_argument('-p',
                        '--port',
                        type=str,
                        default=8080,
                        required=False)
    parser.add_argument('-q',
                        '--query',
                        type=str,
                        default='',
                        required=False)
    parser.add_argument('-l', 
                        '--page_limit', 
                        type=int, 
                        default=0,
                        required=False)

    parser.add_argument('-d', 
                        '--delay', 
                        type=int, 
                        default=0,
                        required=False)

    args = parser.parse_args()

    # We can't set a boolean default for type int argument
    max_pages = False
    if args.page_limit:
        max_pages = args.page_limit

    init(hostname=args.server,
         port=args.port,
         query=args.query,
         max_pages=max_pages,
         delay=args.delay)


if __name__ == '__main__':
    main()
