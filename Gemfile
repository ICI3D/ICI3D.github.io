source 'https://rubygems.org'

# This will help ensure the proper Jekyll version is running.
gem "jekyll"

# Windows does not include zoneinfo files, so bundle the tzinfo-data gem
install_if -> { RUBY_PLATFORM =~ %r!mingw|mswin|java! } do
  gem "tzinfo", "~> 1.2"
  gem "tzinfo-data"
end

# Performance-booster for watching directories on Windows
gem "wdm", "~> 0.1.1", :install_if => Gem.win_platform?

gem 'jekyll-sass-converter'

gem 'jekyll-theme-ici3d', :path => "../jekyll-theme-ici3d"
