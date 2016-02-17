# -*- coding: utf-8 -*-
# Author: Mark Spicer
# License: MIT

import redis
import falcon
import logging.config
import configparser
from apscheduler.schedulers import background as scheduler

from openroast_api import worker
from openroast_api.controllers import recipes


# Read configuration file.
config = configparser.ConfigParser()
config.read('settings.ini')

# Configure logging.
logging.config.fileConfig('settings.ini')
logger = logging.getLogger(__name__)

# Configure scheduler.
sched = scheduler.BackgroundScheduler()
sched.add_job(worker.run, 'interval', seconds=30, id='worker_id')
sched.start()
logger.debug("Created scheduler.")

# Configure database.
db_host = config['db_settings']['host']
db_port = config['db_settings']['port']
db_number = config['db_settings']['number']
db = redis.StrictRedis(host=db_host, port=db_port, db=db_number)
logger.debug("Created database.")

# Create application.
app = falcon.API()
app.add_route('/v1/recipes', recipes.Recipes())
app.add_route('/v1/recipes/{recipe_id}', recipes.Details())
logger.debug("Created application.")
