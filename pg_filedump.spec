%define	pg_version	8.2.6
Summary:	PostgreSQL File Dump Utility
Name:		pg_filedump
Version:	8.2
Release:	1
License:	GPL v2+
Group:		Applications/Databases
Source0:	http://sources.redhat.com/rhdb/tools/%{name}-%{version}.tar
# Source0-md5:	6f052cb339cdb381b21c27eb379abb86
Source1:	ftp://ftp.postgresql.org/pub/source/v%{pg_version}/postgresql-%{pg_version}.tar.bz2
# Source1-md5:	17b9049b4fcad42ee95410833c1db228
URL:		http://sources.redhat.com/rhdb/utilities.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A utility to format PostgreSQL heap, index, and control files into a
human-readable form. You can format/dump the files several ways as
well as dumping straight binary. This utility is intended to aid in
the understanding of the internal contents of a PostgreSQL block.

%prep
%setup -q -a1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	INCLUDE="$(pwd)/postgresql-%{pg_version}/src/include" \
	PGSQL="$(pwd)/postgresql-%{pg_version}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install pg_filedump $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README*
%attr(755,root,root) %{_bindir}/*
