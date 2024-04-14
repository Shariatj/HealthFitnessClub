INSERT INTO Member (Name, Email, DateOfBirth) VALUES
('John Doe', 'john.doe@example.com', '1985-07-12'),
('Alice Smith', 'alice.smith@example.com', '1990-03-05');

INSERT INTO Trainer (Name, AvailabilityStart, AvailabilityEnd) VALUES
('Tom Hardy', '09:00', '17:00'),
('Natalie Portman', '10:00', '18:00');

INSERT INTO Admin (Name) VALUES
('Charles Xavier'),
('Jean Grey');

INSERT INTO FitnessGoals (MemberID, Height, Weight) VALUES
(1, 180.0, 75.0),
(2, 165.0, 60.0);

INSERT INTO HealthMetrics (MemberID, Height, Weight) VALUES
(1, 180.0, 77.0),
(2, 165.0, 58.0);

INSERT INTO Session (Date, Time, TrainerID, MemberID) VALUES
('2023-01-10', '10:00', 1, 1),
('2023-01-11', '11:00', 2, 2);

INSERT INTO Room (RoomName, Date, StartTime, EndTime) VALUES
('Aerobics Room', '2023-01-12', '09:00', '10:00'),
('Weight Room', '2023-01-13', '14:00', '15:00');

INSERT INTO Class (Date, Time, TrainerID, RoomID) VALUES
('2023-01-12', '09:00', 1, 1),
('2023-01-13', '14:00', 2, 2);

INSERT INTO Equipment (EquipmentName, Status) VALUES
('Treadmill Model X', 'Available'),
('Elliptical Model Y', 'In Maintenance');

INSERT INTO Payment (MemberID, Amount, Date) VALUES
(1, 150.00, '2023-01-15'),
(2, 150.00, '2023-01-15');
