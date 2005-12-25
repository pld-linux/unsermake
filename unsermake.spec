%define		_snap		051225

Summary:	An automake replacement by The KDE Team
Summary(pl):	Zamiennik dla automake autorstwa cz�onk�w zespo�u KDE
Name:		unsermake
Version:	%{_snap}
Release:	1
License:	LGPL
Group:		Development/Building
Source0:	ftp://ftp.pld-linux.org/software/kde/%{name}-%{_snap}.tar.bz2
#Source0-md5:	e40206c9244c80ac9a68a216863ae95c
Source1:	%{name}-wrapper.sh
URL:		http://www.kde.me.uk/index.php?page=unsermake
BuildRequires:	rpm-pythonprov
Requires:	python
Requires:	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An automake replacement by The KDE Team.

%description -l pl
Zamiennik dla automake autorstwa cz�onk�w zespo�u KDE.

%package wrapper
Summary:	Unsermake enabling wrapper
Summary(pl):	Wrapper uruchamiajacy unsermake
Group:		Development/Tools
Requires:	%{name} = %{version}-%{release}

%description wrapper
Unsermake enabling wrapper.

%description wrapper -l pl
Wrapper uruchamiajacy unsermake.

%prep
%setup -q -n %{name}

%build

##for i in *.py; 
##do
##%{__python} $i build
##done

%{__python} -c "import compileall; compileall.compile_dir('./')"


%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/%{name}
install -d $RPM_BUILD_ROOT/etc/profile.d
install %{name} *.{py,pyc,um} $RPM_BUILD_ROOT%{_datadir}/%{name}
install %{SOURCE1} $RPM_BUILD_ROOT/etc/profile.d/unsermake.sh
#%%{py_comp} - not working, thou it is the right way probably

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO doc/*.{pdf,obj,sxi,txt}
%dir %{_datadir}/%{name}
%attr(755,root,root) %{_datadir}/%{name}/%{name}
#{_datadir}/%{name}/automake.sudo
%{_datadir}/%{name}/*.py
%{_datadir}/%{name}/*.pyc
%{_datadir}/%{name}/*.um

%files wrapper
%defattr(644,root,root,755)
/etc/profile.d/unsermake.sh
