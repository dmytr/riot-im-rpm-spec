%global debug_package %{nil}
%global __provides_exclude_from %{buildroot}/opt/Riot/resources/app/node_modules
%global __requires_exclude_from %{buildroot}/opt/Riot/resources/app/node_modules
%global __requires_exclude (npm|libnode|libffmpeg)

Name:          riot-im
Version:       0.12.4
Release:       1%{?dist}
Summary:       Riot.im - open team collaboration

License:       Apache 2.0
URL:           https://about.riot.im/
Source0:       riot-web-0.12.4.tar.gz

BuildRequires: rpm
BuildRequires: cpio
BuildRequires: nodejs
BuildRequires: npm
BuildRequires: git

%description
Riot (formerly known as Vector) is a Matrix web client built using
the Matrix React SDK (https://github.com/matrix-org/matrix-react-sdk).

%prep
%autosetup -n riot-web-%{version}
npm install
cp node_modules/matrix-react-sdk/lib/wrappers/WithMatrixClient.js node_modules/matrix-react-sdk/lib/wrappers/withMatrixClient.js
cp node_modules/matrix-js-sdk/lib/Reemitter.js node_modules/matrix-js-sdk/lib/ReEmitter.js
cp config.sample.json config.json

%build
npm run build
npm run install:electron
node_modules/.bin/build -l rpm --x64

%install
rpm2cpio electron_app/dist/riot-web-%{version}.rpm | cpio -idmv -D %{buildroot}

%files
%license LICENSE
%doc CHANGELOG.md
/opt/*
/usr/*

%changelog
* Thu Sep 21 2017 dmytr 0.12.4-1
- Initial packaging
