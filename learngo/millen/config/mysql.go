package config

type MysqlConfig struct {
	PATH     string `mapstructure:"path" yaml:"path" json:"path"`
	PORT     string `mapstructure:"port" yaml:"port" json:"port"`
	DBName   string `mapstructure:"db-name" yaml:"db-name" json:"db-name"`
	UserName string `mapstructure:"username" yaml:"username" json:"username"`
	PassWord string `mapstructure:"password" yaml:"password" json:"password"`
}

func (m *MysqlConfig) Dsn() string {
	return m.UserName + ":" + m.PassWord + "@tcp(" + m.PATH + ":" + m.PORT + ")/" + m.DBName
}
