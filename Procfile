redis_cache: redis-server config/redis_cache.conf
redis_socketio: redis-server config/redis_socketio.conf
redis_queue: redis-server config/redis_queue.conf
web: bench serve
socketio: /usr/bin/node apps/frappe/socketio.js
workerbeat: sh -c 'cd sites && exec ../env/bin/python -m frappe.celery_app beat -s scheduler.schedule'
worker: sh -c 'cd sites && exec ../env/bin/python -m frappe.celery_app worker -n jobs@%h -Ofair --soft-time-limit 360 --time-limit 390'
longjob_worker: sh -c 'cd sites && exec ../env/bin/python -m frappe.celery_app worker -n longjobs@%h -Ofair --soft-time-limit 1500 --time-limit 1530'
async_worker: sh -c 'cd sites && exec ../env/bin/python -m frappe.celery_app worker -n async@%h -Ofair --soft-time-limit 1500 --time-limit 1530'
watch: bench watch