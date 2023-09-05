package global

import (
	"github.com/spf13/viper"
	"go.uber.org/zap"
	"gorm.io/gorm"
	"precheck/config"
)

var (
	PrecheckServer config.Server
	PrecheckViper  *viper.Viper
	PrecheckLog    *zap.Logger
	PrecheckDB     *gorm.DB
)
