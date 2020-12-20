# pré-configuração:
https://github.com/vamperst/Hackaton-exercises-terraform/tree/master/Setup%20e%20Configura%C3%A7%C3%A3o

cd ~/environment

git clone https://github.com/valrsilva/fiap_sre.git

cd fiap_sre/s3

terraform init

terraform apply -auto-approve

## SKIP

#cd ../vpc-call

#terraform init

#terraform apply -auto-approve

#cd ../RT-call

#terraform init

#terraform apply -auto-approve

cd ..

terraform init

terraform workspace new dev

terraform workspace new prod

terraform workspace select dev

terraform init

terraform apply -auto-approve

cd lambda1

virtualenv ~/venv

source ~/venv/bin/activate

mkdir layer

pip3 install -r requirements.txt -t layer

sls deploy

cd ../lambda2

mkdir layer

pip3 install -r requirements.txt -t layer

sls deploy

cd ../lambda3

mkdir layer

pip3 install -r requirements.txt -t layer

sls deploy

## OBS: fazer a subscrição manual no tópico _DEV para receber notificação por e-mail

# REPLICANDO EM PROD

terraform workspace select prod

cd ~/environment/fiap_sre

terraform init

terraform apply -auto-approve

cd lambda1

virtualenv ~/venv

source ~/venv/bin/activate

mkdir layer

pip3 install -r requirements.txt -t layer

## editar o arquivo send.py e trocar as urls das filas para prod

sls deploy --stage prod

cd ../lambda2

mkdir layer

pip3 install -r requirements.txt -t layer

## editar o arquivo serverless.yml e trocar as ARNs das filas para prod

sls deploy --stage prod

cd ../lambda3

mkdir layer

pip3 install -r requirements.txt -t layer

## editar o arquivo serverless.yml e send_to_topic.py e trocar as ARNs/URLs das filas para prod

sls deploy --stage prod

## OBS: fazer a subscrição manual no tópico _PROD para receber notificação por e-mail
