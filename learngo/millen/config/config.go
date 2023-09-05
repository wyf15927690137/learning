package config

type Server struct {
	JenkinsInfo JenkinsInfo `mapstructure:"jenkinsinfo" json:"jenkinsinfo" yaml:"jenkinsinfo"`
	MysqlConfig MysqlConfig `mapstructure:"mysql" json:"mysql" yaml:"mysql"`
	Zap         Zap         `mapstructure:"zap" json:"zap" yaml:"zap"`
}
