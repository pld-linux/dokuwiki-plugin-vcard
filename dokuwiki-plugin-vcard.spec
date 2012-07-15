%define		plugin		vcard
%define		php_min_version 5.0.0
%include	/usr/lib/rpm/macros.php
Summary:	DokuWiki vCard/hCard plugin
Name:		dokuwiki-plugin-%{plugin}
Version:	20070516
Release:	1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://tomas.valenta.cz/dokuwiki/vcard-plugin.zip
# Source0-md5:	a0d6543e1317debfb3b03bb9ffc7a603
URL:		http://www.dokuwiki.org/plugin:vcard
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.520
Requires:	dokuwiki >= 20061106
Requires:	php-common >= 4:%{php_min_version}
Requires:	php-date
Requires:	php-pcre
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		dokuconf	/etc/webapps/dokuwiki
%define		dokudir		/usr/share/dokuwiki
%define		plugindir	%{dokudir}/lib/plugins/%{plugin}

%description
This plugin lets you create vCard files on the fly in your wiki, which
other users can download and add to their addressbook. With the folded
plugin installed, you can unfold information about the person right in
your wiki.

%prep
%setup -qc
mv %{plugin}/* .

version=$(awk -F"'" '/date/&&/=>/{print $4}' syntax.php)
if [ "$(echo "$version" | tr -d -)" != %{version} ]; then
	: %%{version} mismatch
	exit 1
fi

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a . $RPM_BUILD_ROOT%{plugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{plugindir}
%{plugindir}/*.php
%{plugindir}/*.gif
