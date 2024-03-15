import pymysql

connection = pymysql.connect(
    host='your_host',
    user='your_username',
    password='your_password',
    database='python_busbooking'  
)


cursor = connection.cursor()

create_bus_booking_table = """
CREATE TABLE IF NOT EXISTS bus_booking (
    booking_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    bus_id INT NOT NULL,
    passenger_name VARCHAR(255) NOT NULL,
    gender VARCHAR(20) NOT NULL,
    no_of_seats INT NOT NULL,
    mobile_no VARCHAR(255) NOT NULL,
    age INT NOT NULL,
    Amount INT,
    boarding_station VARCHAR(100),
    boarding_date DATE,
    booking_date DATE NOT NULL,
    FOREIGN KEY (bus_id) REFERENCES busdetail(bus_id)
);
"""

create_bus_operator_table = """
CREATE TABLE IF NOT EXISTS bus_operator (
    operator_id INT NOT NULL PRIMARY KEY,
    name VARCHAR(100),
    address VARCHAR(255),
    phone VARCHAR(20),
    email VARCHAR(100),
    bus_id INT
);
"""

create_bus_route_table = """
CREATE TABLE IF NOT EXISTS bus_route (
    bus_id INT,
    station_name VARCHAR(100),
    destination_name VARCHAR(100),
    FOREIGN KEY (bus_id) REFERENCES busdetail(bus_id)
);
"""

create_bus_detail_table = """
CREATE TABLE IF NOT EXISTS busdetail (
    bus_id INT NOT NULL PRIMARY KEY,
    capacity INT,
    operator_id INT,
    bus_type VARCHAR(50),
    fare_rs DECIMAL(10,2),
    route_id INT,
    FOREIGN KEY (operator_id) REFERENCES bus_operator(operator_id)
);
"""

create_running_detail_table = """
CREATE TABLE IF NOT EXISTS runningdetail (
    bus_id INT,
    running_date DATE,
    seat_available INT,
    FOREIGN KEY (bus_id) REFERENCES busdetail(bus_id)
);
"""

create_tables_queries = [
    create_bus_booking_table,
    create_bus_operator_table,
    create_bus_route_table,
    create_bus_detail_table,
    create_running_detail_table
]

for query in create_tables_queries:
    cursor.execute(query)


connection.commit()
connection.close()

print("Tables created successfully!")
