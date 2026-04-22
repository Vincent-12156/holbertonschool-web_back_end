
# NoSQL
MongoDB is a document-oriented and NoSQL database solution that provides great scalability and flexibility along with a powerful querying system. With MongoDB and Python, you can develop many different types of database applications quickly. So if your Python application needs a database that’s just as flexible as the language itself, then MongoDB is for you.

## Install MongoDB 4.4 (Ubuntu 22.04)
1. Install the missing libssl1.1 dependency

MongoDB 4.x requires OpenSSL 1.1, which isn’t included in Ubuntu 22.04.
```
echo "deb http://security.ubuntu.com/ubuntu focal-security main" | sudo tee /etc/apt/sources.list.d/focal-security.list
sudo apt update
sudo apt install -y libssl1.1
sudo rm /etc/apt/sources.list.d/focal-security.list
sudo apt update
```
2. Add the MongoDB 4.4 repository and key
```
curl -fsSL https://www.mongodb.org/static/pgp/server-4.4.asc | sudo apt-key add -
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/4.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.4.list
sudo apt update
```
3. Install MongoDB 4.4 packages
```
sudo apt install -y mongodb-org
```
4. Prepare required directories and permissions
```
sudo mkdir -p /var/lib/mongodb /var/log/mongodb
sudo chown -R mongodb:mongodb /var/lib/mongodb /var/log/mongodb
```
5. Start mongod
```
sudo -u mongodb /usr/bin/mongod --config /etc/mongod.conf &
```
This runs MongoDB in the foreground.

### Verification
Check the MongoDB version:
```
mongod --version
```
Expected output should show something like v4.4.xx.