CREATE DATABASE boardwatch
    WITH
    ENCODING = 'UTF8';

CREATE EXTENSION "uuid-ossp";

CREATE TABLE users (
	id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
	username varchar() NOT NULL UNIQUE,
	email varchar() NOT NULL UNIQUE,
	created_at timestamptz NOT NULL DEFAULT (now() AT TIME ZONE 'utc')
);

CREATE TABLE platform_families (
	id int GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
	name varchar() NULL UNIQUE, -- char limit 100
	generation smallint NULL,
	developer varchar() NULL -- char limit 100
);

CREATE TABLE platform_name_groups (
	id int GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
	name varchar() NULL UNIQUE, -- char limit 50
	description varchar() NULL -- char limit 100
);

CREATE TABLE platforms (
	id int GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
	name varchar() NULL, -- char limit 100
	platform_family_id smallint NULL REFERENCES platform_families(id),
	name_group_id smallint NULL REFERENCES platform_name_groups(id),
	is_brand_missing boolean NOT NULL,
	model_no varchar() NULL, -- char limit 100
	storage_capacity varchar() NULL, -- char limit 100
	description text NULL,
	disambiguation varchar() NULL, -- char limit 100
	relevance smallint NULL -- (#/10)
);

CREATE TABLE colors (
	id int GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
	name varchar() UNIQUE NOT NULL -- char limit 50?
);

CREATE TABLE platform_editions (
	id int GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
	name varchar() NULL, -- char limit 100
	platform_id smallint NULL REFERENCES platforms(id),
	official_color varchar() NULL, -- char limit 60
	has_matte boolean NULL,
	has_transparency boolean NULL,
	has_gloss boolean NULL,
	note text NULL,
	image_url text NULL
);

CREATE TABLE colors_platform_editions (
	platform_edition_id int NOT NULL REFERENCES platform_editions(id),
	color_id smallint NOT NULL REFERENCES colors(id),
	PRIMARY KEY (platform_edition_id, color_id)
);

CREATE TABLE game_series (
	id int GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
	name varchar() UNIQUE, -- char limit 150
	description varchar() -- char limit 255
)

CREATE TABLE game_families (
	id int GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
	name varchar() NOT NULL UNIQUE -- char limit 255
)

CREATE TABLE games (
	id int GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
	name varchar() NOT NULL, -- char limit 255
	year_first_release smallint NULL,
	is_bootleg boolean NOT NULL
);

CREATE TABLE game_families_games (
	game_id integer NOT NULL REFERENCES games(id),
	game_family_id integer NOT NULL REFERENCES game_families(id),
	PRIMARY KEY (game_family_id, game_id)
)

CREATE TABLE game_series_games (
	game_id integer NOT NULL REFERENCES games(id),
	game_series_id integer NOT NULL REFERENCES game_series(id),
	PRIMARY KEY (game_series_id, game_id)
)

CREATE TABLE games_platforms_compatibility (
	platform_id int NOT NULL REFERENCES platforms(id),
	game_id int NOT NULL REFERENCES games(id),
	PRIMARY KEY (platform_id, game_id)
);

CREATE TABLE accessory_types (
	id int GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
	name varchar() NOT NULL UNIQUE, -- char limit 100
	description varchar() NULL -- char limit 255
);

CREATE TABLE accessories (
	id int GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
	name varchar() NOT NULL, -- char limit 255
	type smallint NOT NULL REFERENCES accessory_types(id),
	year_first_release smallint NULL,
	is_first_party boolean NOT NULL,
	description text
);

CREATE TABLE accessories_games_compatibility (
	game_id int NOT NULL REFERENCES games(id),
	accessory_id int NOT NULL REFERENCES accessories(id),
	PRIMARY KEY (game_id, accessory_id)
);

CREATE TABLE accessories_platforms_compatibility (
	platform_id int NOT NULL REFERENCES platforms(id),
	accessory_id int NOT NULL REFERENCES accessories(id),
	PRIMARY KEY (platform_id, accessory_id)
);

CREATE TABLE accessory_variations (
	id int GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
	accessory_id int NOT NULL REFERENCES accessories(id),
	description varchar() NOT NULL -- char limit 255
);

CREATE TABLE accessory_variations_colors (
	accessory_variation_id int NOT NULL REFERENCES accessory_variations(id),
	color_id int NOT NULL REFERENCES colors(id),
	PRIMARY KEY (accessory_variation_id, color_id)
);

CREATE TABLE characters (
	id int GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
	name varchar() NOT NULL, -- char limit 150
	name_disambiguation varchar() NULL, -- char limit 150
	from_what varchar() NOT NULL -- char limit 255
);

CREATE TABLE characters_in_games (
	character_id int NOT NULL REFERENCES characters(id),
	game_id int NOT NULL REFERENCES games(id),
	PRIMARY KEY (character_id, game_id),
	is_playable boolean NOT NULL,
	playability_extent text NULL
);

-- CREATE TABLE users_platforms (
-- 	user_id uuid NOT NULL REFERENCES users(id),
-- 	platform_id int NOT NULL REFERENCES platforms(id),
-- 	is_edition_ambivalent boolean NOT NULL
-- );

CREATE TABLE watchlist_platform_editions (
	user_id uuid NOT NULL REFERENCES users(id),
	platform_edition_id int NOT NULL REFERENCES platforms(id),
	PRIMARY KEY (user_id, platform_edition_id)
);
