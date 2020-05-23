from proxypool.api import app
from proxypool.Scheduler import Scheduler
def main():
    s = Scheduler()
    s.run()
    app.run()

if __name__ == '__main__':
    main()