-- Пользователи
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email TEXT UNIQUE NOT NULL,
    phone TEXT,
    fam TEXT,
    name TEXT,
    otc TEXT
);

-- Уровни сложности
CREATE TABLE levels (
    id SERIAL PRIMARY KEY,
    winter TEXT,
    summer TEXT,
    autumn TEXT,
    spring TEXT
);

-- Координаты
CREATE TABLE coords (
    id SERIAL PRIMARY KEY,
    latitude DOUBLE PRECISION,
    longitude DOUBLE PRECISION,
    height INTEGER
);

-- Перевалы
CREATE TABLE pereval (
    id SERIAL PRIMARY KEY,
    beauty_title TEXT,
    title TEXT,
    other_titles TEXT,
    connect TEXT,
    add_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    user_id INT REFERENCES users(id),
    coords_id INT REFERENCES coords(id),
    level_id INT REFERENCES levels(id),
    status TEXT NOT NULL DEFAULT 'new' CHECK (
        status IN ('new', 'pending', 'accepted', 'rejected')
    )
);

-- Изображения
CREATE TABLE images (
    id SERIAL PRIMARY KEY,
    pereval_id INT REFERENCES pereval(id) ON DELETE CASCADE,
    title TEXT,
    img BYTEA,
    date_added TIMESTAMP DEFAULT now()
);

-- Справочник активностей
CREATE TABLE spr_activities_types (
    id SERIAL PRIMARY KEY,
    title TEXT
);

-- Горные районы
CREATE TABLE pereval_areas (
    id SERIAL PRIMARY KEY,
    id_parent INT,
    title TEXT
);
