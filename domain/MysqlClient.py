from config.envion import env_config
from dao.relation_client import MysqlClient

mysql_client = MysqlClient(host=env_config.get("mysql_host"), port=env_config.get("mysql_prot"),
                           user=env_config.get("mysql_user"), password=env_config.get("mysql_password"),
                           dbname="huang")