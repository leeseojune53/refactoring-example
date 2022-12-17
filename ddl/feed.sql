create table feed
(
    id         varchar(36) not null
        primary key,
    user_id    varchar(36) null,
    user_name  varchar(20) null,
    comments   text        null,
    created_at timestamp   null
);

INSERT INTO refactor.feed (id, user_id, user_name, comments, created_at) VALUES ('3d436093-2451-4917-be06-f000a6d27771', '3d436093-2451-4917-be06-f000a6d27772', 'hihihi', '[{"content": "이거 완전 0등", "ttabong": 100, "user_id": "3d436093-2451-4917-be06-f000a6d27772", "user_name": "나이름바꿈"}]', '2022-12-18 01:10:59');
INSERT INTO refactor.feed (id, user_id, user_name, comments, created_at) VALUES ('3d436093-2451-4917-be06-f000a6d27774', '3d436093-2451-4917-be06-f000a6d27774', 'arthur', '[{"content": "이거 완전 1등", "ttabong": 12, "user_id": "3d436093-2451-4917-be06-f000a6d27774", "user_name": "arthur"},{"content": "이거 완전 2등", "ttabong": 10, "user_id": "3d436093-2451-4917-be06-f000a6d27772", "user_name": "hihi"}]', '2022-12-18 01:10:59');
