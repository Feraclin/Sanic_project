--
-- PostgreSQL database dump
--

-- Dumped from database version 14.4 (Ubuntu 14.4-0ubuntu0.22.04.1)
-- Dumped by pg_dump version 15.0

-- Started on 2022-10-31 00:21:42

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
-- TOC entry 3353 (class 0 OID 80625)
-- Dependencies: 213
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: feraclin
--

COPY public.users (id, username, password, is_admin, active) FROM stdin;
1	default_admin	a7c3fce0af38fcb83c2f6adfa53ab220e9b1d739e2208a665ffa54267bbc8781	t	t
2	test_user	a7c3fce0af38fcb83c2f6adfa53ab220e9b1d739e2208a665ffa54267bbc8781	f	t
59	another_user	5994471abb01112afcc18159f6cc74b4f511b99806da59b3caf5a9c173cacfc5	f	t
\.


--
-- TOC entry 3355 (class 0 OID 80636)
-- Dependencies: 215
-- Data for Name: account; Type: TABLE DATA; Schema: public; Owner: feraclin
--

COPY public.account (id, balance, owner) FROM stdin;
2	2000	1
3	0	2
1	900	2
\.


--
-- TOC entry 3349 (class 0 OID 80506)
-- Dependencies: 209
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: feraclin
--

COPY public.alembic_version (version_num) FROM stdin;
ba38149cb896
\.


--
-- TOC entry 3351 (class 0 OID 80614)
-- Dependencies: 211
-- Data for Name: good; Type: TABLE DATA; Schema: public; Owner: feraclin
--

COPY public.good (id, title, description, cost) FROM stdin;
1	good1	cheap good	1
2	good2	expensive good	100
3	good3	luxury good	100000
\.


--
-- TOC entry 3357 (class 0 OID 80648)
-- Dependencies: 217
-- Data for Name: transaction; Type: TABLE DATA; Schema: public; Owner: feraclin
--

COPY public.transaction (id, amount, destination_account) FROM stdin;
1	800	1
2	200	1
1234567	1000	2
\.


--
-- TOC entry 3363 (class 0 OID 0)
-- Dependencies: 214
-- Name: account_id_seq; Type: SEQUENCE SET; Schema: public; Owner: feraclin
--

SELECT pg_catalog.setval('public.account_id_seq', 2, true);


--
-- TOC entry 3364 (class 0 OID 0)
-- Dependencies: 210
-- Name: good_id_seq; Type: SEQUENCE SET; Schema: public; Owner: feraclin
--

SELECT pg_catalog.setval('public.good_id_seq', 8, true);


--
-- TOC entry 3365 (class 0 OID 0)
-- Dependencies: 216
-- Name: transaction_id_seq; Type: SEQUENCE SET; Schema: public; Owner: feraclin
--

SELECT pg_catalog.setval('public.transaction_id_seq', 2, true);


--
-- TOC entry 3366 (class 0 OID 0)
-- Dependencies: 212
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: feraclin
--

SELECT pg_catalog.setval('public.users_id_seq', 83, true);


-- Completed on 2022-10-31 00:21:42

--
-- PostgreSQL database dump complete
--

