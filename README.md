# account-balance
This repository is the solution to process a csv file with banking account information and then sending an email to the user. The csv file has the account id follows by an underscore symbol and then the email.

The csv file is in data folder inside the repository it's aab43a27-48b2-4249-954e-a2629220ff11_aniel.villegas@yahoo.com.csv If you want to replace the email you just need to change "aniel.villegas@yahoo.com" with your email, for example "my_personal_email@particulardomain.com".

The following are the steps to send the email.

1. Clone the repository:

In your folder execute 

git clone https://github.com/anielv95/account-balance.git

2. Go inside the repository folder and execute:

cd account-balance

3. Create a virtual environment.

python -m venv .account-balance

4. Build the containers.

Execute:

    1. cd src
    2. docker build -t processing -f processing.dockerfile .
    3. cd email
    4. docker build -t email -f email.dockerfile .

5. Raise the network with the containers ready to get requests.

Execute:

    1. cd ../..
    2. docker-compose up




