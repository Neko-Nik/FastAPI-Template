## The script is used to restart the gpt api
## Change the path of the virtualenv and the gunicorn command accordingly

#stop the api , if its already running at port 443
fuser -n tcp -k 443

#start the gpt api
cd /home/neko/template && source virtualenv/bin/activate

#start the gpt api
gunicorn --workers=3 --threads=3 --reload --bind 0.0.0.0:443 --timeout 2500 --keyfile=/home/neko/privkey.pem --certfile=/home/neko/fullchain.pem --reload --capture-output --error-logfile logs/error_log.txt --access-logfile logs/guicorn_log.txt -k uvicorn.workers.UvicornWorker app:app &