
%define		_snap		040511
%define		_packager	adgor

Summary:	An automake replacement by The KDE Team
Summary(pl):	Zamiennik dla automake autorstwa cz³onków zespo³u KDE
Name:		unsermake
Version:	%{_snap}
Release:	1
License:	LGPL
Group:		Development/Building
Source0:	http://ep09.pld-linux.org/~%{_packager}/kde/%{name}-%{_snap}.tar.bz2
# Source0-md5:	f2ca222dcce8fbed9beea5a4347c355d
URL:		http://www.kde.org/
BuildRequires:	python-modules
Requires:	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An automake replacement by The KDE Team.

%description -l pl
Zamiennik dla automake autorstwa cz³onków zespo³u KDE.

%prep
%setup -q -n %{name}-%{_snap}

##for i in *.py; 
##do
##%{__python} $i build
##done
%{__python} -c "import compileall; compileall.compile_dir('./')"
%build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/%{name}
install automake.sudo %{name} *.{py,pyc,um} $RPM_BUILD_ROOT%{_datadir}/%{name}
#%%{py_comp} - not working, thou it is the right way probably

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO doc/*.{pdf,obj,sxi,txt}
%dir %{_datadir}/%{name}
%attr(755,root,root) %{_datadir}/%{name}/%{name}
%{_datadir}/%{name}/automake.sudo
%{_datadir}/%{name}/*.py
%{_datadir}/%{name}/*.pyc
%{_datadir}/%{name}/*.um
