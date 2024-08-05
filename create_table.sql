CREATE TABLE IF NOT EXISTS users(
    name VARCHAR(60),
    birth VARCHAR(10),
    job VARCHAR(60),
    company VARCHAR(60),
    country_id FOREIGN KEY(country_id) references country(country_id),
    city_id FOREIGN KEY(city_id) references city(city_id),
    address VARCHAR(60),
    zip_code VARCHAR(5),                                         
    phone VARCHAR(20),
    email VARCHAR(60),
    card_number VARCHAR(20),
    card_expire VARCHAR(5),
    security_code VARCHAR(4),
    url VARCHAR(20))

CREATE TABLE IF NOT EXISTS country(
    country_id INT PRIMARY KEY AUTO_INCRIMENT,    
    country VARCHAR(30)
    )
    
CREATE TABLE IF NOT EXISTS city(
        city_id INT PRIMARY KEY AUTO_INCRIMENT,
        city VARCHAR(30)
    )