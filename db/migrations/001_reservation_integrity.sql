-- Maintenance enhancement: enforce reservation data integrity.
-- Run after importing db/lms.sql.

ALTER TABLE `reserve`
  ADD UNIQUE KEY `uniq_user_book_reservation` (`user_id`, `book_id`),
  ADD KEY `idx_reserve_user_id` (`user_id`),
  ADD KEY `idx_reserve_book_id` (`book_id`);

ALTER TABLE `reserve`
  ADD CONSTRAINT `fk_reserve_user`
    FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
    ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_reserve_book`
    FOREIGN KEY (`book_id`) REFERENCES `books` (`id`)
    ON DELETE CASCADE ON UPDATE CASCADE;
