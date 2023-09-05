package initialize

import (
	"gorm.io/driver/mysql"
	"gorm.io/gorm"
	"precheck/global"
)

func GormMysql() *gorm.DB {
	m := global.PrecheckServer.MysqlConfig
	if m.DBName == "" {
		return nil
	}

	mysqlConfig := mysql.Config{
		DSN:                       m.Dsn(),
		DefaultStringSize:         191,
		SkipInitializeWithVersion: false,
	}

	if db, err := gorm.Open(mysql.New(mysqlConfig)); err != nil {
		return nil
	} else {
		return db
	}
}
