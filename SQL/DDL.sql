-- Drop existing tables if they exist to prevent errors on creation
DROP TABLE IF EXISTS Payment CASCADE;
DROP TABLE IF EXISTS Equipment CASCADE;
DROP TABLE IF EXISTS Class CASCADE;
DROP TABLE IF EXISTS Room CASCADE;
DROP TABLE IF EXISTS Session CASCADE;
DROP TABLE IF EXISTS HealthMetrics CASCADE;
DROP TABLE IF EXISTS FitnessGoals CASCADE;
DROP TABLE IF EXISTS Admin CASCADE;
DROP TABLE IF EXISTS Trainer CASCADE;
DROP TABLE IF EXISTS Member CASCADE;

-- Create tables
CREATE TABLE Member (
    MemberID SERIAL PRIMARY KEY,
    Name VARCHAR(255),
    Email VARCHAR(255),
    DateOfBirth DATE
);

CREATE TABLE Trainer (
    TrainerID SERIAL PRIMARY KEY,
    Name VARCHAR(255),
    AvailabilityStart TIME,
    AvailabilityEnd TIME
);

CREATE TABLE Admin (
    AdminID SERIAL PRIMARY KEY,
    Name VARCHAR(255)
);

CREATE TABLE FitnessGoals (
    GoalID SERIAL PRIMARY KEY,
    MemberID INT REFERENCES Member(MemberID),
    Height DECIMAL(10, 2),
    Weight DECIMAL(10, 2)
);

CREATE TABLE HealthMetrics (
    MetricID SERIAL PRIMARY KEY,
    MemberID INT REFERENCES Member(MemberID),
    Height DECIMAL(10, 2),
    Weight DECIMAL(10, 2)
);

CREATE TABLE Session (
    SessionID SERIAL PRIMARY KEY,
    Date DATE,
    Time TIME,
    TrainerID INT REFERENCES Trainer(TrainerID),
    MemberID INT REFERENCES Member(MemberID)
);

CREATE TABLE Room (
    RoomID SERIAL PRIMARY KEY,
    RoomName VARCHAR(255),
    Date DATE,
    StartTime TIME,
    EndTime TIME
);

CREATE TABLE Class (
    ClassID SERIAL PRIMARY KEY,
    Date DATE,
    Time TIME,
    TrainerID INT REFERENCES Trainer(TrainerID),
    RoomID INT REFERENCES Room(RoomID)
);

CREATE TABLE Equipment (
    EquipmentID SERIAL PRIMARY KEY,
    EquipmentName VARCHAR(255),
    Status VARCHAR(100)
);

CREATE TABLE Payment (
    PaymentID SERIAL PRIMARY KEY,
    MemberID INT REFERENCES Member(MemberID),
    Amount DECIMAL(10, 2),
    Date DATE
);








