--
-- PostgreSQL database dump
--

-- Dumped from database version 14.4 (Ubuntu 14.4-0ubuntu0.22.04.1)
-- Dumped by pg_dump version 15.0

-- Started on 2022-10-30 23:59:51

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 4 (class 2615 OID 2200)
-- Name: public; Type: SCHEMA; Schema: -; Owner: postgres
--

-- *not* creating schema, since initdb creates it


ALTER SCHEMA public OWNER TO postgres;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 215 (class 1259 OID 80636)
-- Name: account; Type: TABLE; Schema: public; Owner: feraclin
--

CREATE TABLE public.account (
    id integer NOT NULL,
    balance integer NOT NULL,
    owner integer NOT NULL
);


ALTER TABLE public.account OWNER TO feraclin;

--
-- TOC entry 214 (class 1259 OID 80635)
-- Name: account_id_seq; Type: SEQUENCE; Schema: public; Owner: feraclin
--

CREATE SEQUENCE public.account_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.account_id_seq OWNER TO feraclin;

--
-- TOC entry 3368 (class 0 OID 0)
-- Dependencies: 214
-- Name: account_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: feraclin
--

ALTER SEQUENCE public.account_id_seq OWNED BY public.account.id;


--
-- TOC entry 209 (class 1259 OID 80506)
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: feraclin
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO feraclin;

--
-- TOC entry 211 (class 1259 OID 80614)
-- Name: good; Type: TABLE; Schema: public; Owner: feraclin
--

CREATE TABLE public.good (
    id integer NOT NULL,
    title character varying(255) NOT NULL,
    description character varying(255) NOT NULL,
    cost integer NOT NULL
);


ALTER TABLE public.good OWNER TO feraclin;

--
-- TOC entry 210 (class 1259 OID 80613)
-- Name: good_id_seq; Type: SEQUENCE; Schema: public; Owner: feraclin
--

CREATE SEQUENCE public.good_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.good_id_seq OWNER TO feraclin;

--
-- TOC entry 3369 (class 0 OID 0)
-- Dependencies: 210
-- Name: good_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: feraclin
--

ALTER SEQUENCE public.good_id_seq OWNED BY public.good.id;


--
-- TOC entry 217 (class 1259 OID 80648)
-- Name: transaction; Type: TABLE; Schema: public; Owner: feraclin
--

CREATE TABLE public.transaction (
    id integer NOT NULL,
    amount integer NOT NULL,
    destination_account integer NOT NULL
);


ALTER TABLE public.transaction OWNER TO feraclin;

--
-- TOC entry 216 (class 1259 OID 80647)
-- Name: transaction_id_seq; Type: SEQUENCE; Schema: public; Owner: feraclin
--

CREATE SEQUENCE public.transaction_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.transaction_id_seq OWNER TO feraclin;

--
-- TOC entry 3370 (class 0 OID 0)
-- Dependencies: 216
-- Name: transaction_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: feraclin
--

ALTER SEQUENCE public.transaction_id_seq OWNED BY public.transaction.id;


--
-- TOC entry 213 (class 1259 OID 80625)
-- Name: users; Type: TABLE; Schema: public; Owner: feraclin
--

CREATE TABLE public.users (
    id integer NOT NULL,
    username character varying(255) NOT NULL,
    password character varying(255) NOT NULL,
    is_admin boolean,
    active boolean
);


ALTER TABLE public.users OWNER TO feraclin;

--
-- TOC entry 212 (class 1259 OID 80624)
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: feraclin
--

CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_id_seq OWNER TO feraclin;

--
-- TOC entry 3371 (class 0 OID 0)
-- Dependencies: 212
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: feraclin
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- TOC entry 3196 (class 2604 OID 80639)
-- Name: account id; Type: DEFAULT; Schema: public; Owner: feraclin
--

ALTER TABLE ONLY public.account ALTER COLUMN id SET DEFAULT nextval('public.account_id_seq'::regclass);


--
-- TOC entry 3194 (class 2604 OID 80617)
-- Name: good id; Type: DEFAULT; Schema: public; Owner: feraclin
--

ALTER TABLE ONLY public.good ALTER COLUMN id SET DEFAULT nextval('public.good_id_seq'::regclass);


--
-- TOC entry 3197 (class 2604 OID 80651)
-- Name: transaction id; Type: DEFAULT; Schema: public; Owner: feraclin
--

ALTER TABLE ONLY public.transaction ALTER COLUMN id SET DEFAULT nextval('public.transaction_id_seq'::regclass);


--
-- TOC entry 3195 (class 2604 OID 80628)
-- Name: users id; Type: DEFAULT; Schema: public; Owner: feraclin
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- TOC entry 3359 (class 0 OID 80636)
-- Dependencies: 215
-- Data for Name: account; Type: TABLE DATA; Schema: public; Owner: feraclin
--

COPY public.account (id, balance, owner) FROM stdin;
2	2000	1
3	0	2
1	900	2
\.


--
-- TOC entry 3353 (class 0 OID 80506)
-- Dependencies: 209
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: feraclin
--

COPY public.alembic_version (version_num) FROM stdin;
ba38149cb896
\.


--
-- TOC entry 3355 (class 0 OID 80614)
-- Dependencies: 211
-- Data for Name: good; Type: TABLE DATA; Schema: public; Owner: feraclin
--

COPY public.good (id, title, description, cost) FROM stdin;
1	good1	cheap good	1
2	good2	expensive good	100
3	good3	luxury good	100000
\.


--
-- TOC entry 3361 (class 0 OID 80648)
-- Dependencies: 217
-- Data for Name: transaction; Type: TABLE DATA; Schema: public; Owner: feraclin
--

COPY public.transaction (id, amount, destination_account) FROM stdin;
1	800	1
2	200	1
1234567	1000	2
\.


--
-- TOC entry 3357 (class 0 OID 80625)
-- Dependencies: 213
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: feraclin
--

COPY public.users (id, username, password, is_admin, active) FROM stdin;
1	default_admin	a7c3fce0af38fcb83c2f6adfa53ab220e9b1d739e2208a665ffa54267bbc8781	t	t
2	test_user	a7c3fce0af38fcb83c2f6adfa53ab220e9b1d739e2208a665ffa54267bbc8781	f	t
59	another_user	5994471abb01112afcc18159f6cc74b4f511b99806da59b3caf5a9c173cacfc5	f	t
\.


--
-- TOC entry 3372 (class 0 OID 0)
-- Dependencies: 214
-- Name: account_id_seq; Type: SEQUENCE SET; Schema: public; Owner: feraclin
--

SELECT pg_catalog.setval('public.account_id_seq', 2, true);


--
-- TOC entry 3373 (class 0 OID 0)
-- Dependencies: 210
-- Name: good_id_seq; Type: SEQUENCE SET; Schema: public; Owner: feraclin
--

SELECT pg_catalog.setval('public.good_id_seq', 8, true);


--
-- TOC entry 3374 (class 0 OID 0)
-- Dependencies: 216
-- Name: transaction_id_seq; Type: SEQUENCE SET; Schema: public; Owner: feraclin
--

SELECT pg_catalog.setval('public.transaction_id_seq', 2, true);


--
-- TOC entry 3375 (class 0 OID 0)
-- Dependencies: 212
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: feraclin
--

SELECT pg_catalog.setval('public.users_id_seq', 83, true);


--
-- TOC entry 3209 (class 2606 OID 80641)
-- Name: account account_pkey; Type: CONSTRAINT; Schema: public; Owner: feraclin
--

ALTER TABLE ONLY public.account
    ADD CONSTRAINT account_pkey PRIMARY KEY (id);


--
-- TOC entry 3199 (class 2606 OID 80510)
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: feraclin
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- TOC entry 3201 (class 2606 OID 80621)
-- Name: good good_pkey; Type: CONSTRAINT; Schema: public; Owner: feraclin
--

ALTER TABLE ONLY public.good
    ADD CONSTRAINT good_pkey PRIMARY KEY (id);


--
-- TOC entry 3203 (class 2606 OID 80623)
-- Name: good good_title_key; Type: CONSTRAINT; Schema: public; Owner: feraclin
--

ALTER TABLE ONLY public.good
    ADD CONSTRAINT good_title_key UNIQUE (title);


--
-- TOC entry 3211 (class 2606 OID 80653)
-- Name: transaction transaction_pkey; Type: CONSTRAINT; Schema: public; Owner: feraclin
--

ALTER TABLE ONLY public.transaction
    ADD CONSTRAINT transaction_pkey PRIMARY KEY (id);


--
-- TOC entry 3205 (class 2606 OID 80632)
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: feraclin
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- TOC entry 3207 (class 2606 OID 80634)
-- Name: users users_username_key; Type: CONSTRAINT; Schema: public; Owner: feraclin
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_username_key UNIQUE (username);


--
-- TOC entry 3212 (class 2606 OID 80642)
-- Name: account account_owner_fkey; Type: FK CONSTRAINT; Schema: public; Owner: feraclin
--

ALTER TABLE ONLY public.account
    ADD CONSTRAINT account_owner_fkey FOREIGN KEY (owner) REFERENCES public.users(id) ON DELETE CASCADE;


--
-- TOC entry 3213 (class 2606 OID 80654)
-- Name: transaction transaction_destination_account_fkey; Type: FK CONSTRAINT; Schema: public; Owner: feraclin
--

ALTER TABLE ONLY public.transaction
    ADD CONSTRAINT transaction_destination_account_fkey FOREIGN KEY (destination_account) REFERENCES public.account(id) ON DELETE CASCADE;


--
-- TOC entry 3367 (class 0 OID 0)
-- Dependencies: 4
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE USAGE ON SCHEMA public FROM PUBLIC;
GRANT ALL ON SCHEMA public TO PUBLIC;


-- Completed on 2022-10-30 23:59:52

--
-- PostgreSQL database dump complete
--

