# CSTK
Cyber Security Tool Kit

This project downloads and installs required tools for pen-testing, and data analysis. It is built and designed with the intent to integrate into any existing tools such as Wigle, Trello, JIRA, and/or Slack while following KISS principles. This tool kit is meant to simplify pen-testing for developers and engineers to secure their products and/or code. The main goal is to be able to use this tool kit without requiring specialized training.

## Getting Started


### Prerequisites

This has been developed and tested on Ubuntu 18.04.3 LTS.

### Installing

You will need to run setup_cstk.sh either as root or with sudo

```
sudo ./setup_cstk.sh
```

## Running the tests

TODO

## Deployment

You will need to start honcho either as root or with sudo

TODO:
* Honcho ProcFile setup via setup_cstk.sh or create_env.py

```
sudo su
source venv/bin/activate
honcho start
```

## Built With

* [Django](https://github.com/django/django) - The web framework used
* [Django Rest Framework](https://github.com/encode/django-rest-framework) - toolkit for building Web APIs
* [Celery](https://github.com/celery/celery) - asynchronous task queue/job queue based on distributed message passing
* [RabbitMQ](https://github.com/rabbitmq/rabbitmq-server) - message broker for Celery
* [Honcho](https://github.com/nickstenning/honcho) - Multiplexing multiple processes output
* [Django-environ](https://github.com/joke2k/django-environ) - Configure CSTK settings.py with .env file
* [Django Extensions](https://github.com/django-extensions/django-extensions) - collection of custom extensions

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/Great-Lakes-Cyber-Services/CSTK/tags). 

## Authors

TODO

## License

This project is licensed under the GPLv3 - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* [PurpleBooth](https://github.com/PurpleBooth)
* [darkmatter0](https://github.com/darkmatter0)
* [ksarthak4ever](https://github.com/ksarthak4ever)
* [al45tair](https://github.com/al45tair)
