package main

import (
    "gorm.io/driver/postgres"
    "gorm.io/gorm"
)

func main() {
    // Database connection string
    dsn := "host=127.0.0.1 user=postgres password=000000 dbname=mille port=5432 sslmode=disable"

    // Open a connection to the database
    _, err := gorm.Open(postgres.Open(dsn), &gorm.Config{})
    if err != nil {
        // Handle the error if the connection fails
        panic("failed to connect to database")
    }

    // defer db.Close()

    // Use the `db` object to perform database operations
    // ...
}