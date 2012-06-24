
%define		beta	beta2

Summary:	Intuitive tool for burning CDs
Summary(pl.UTF-8):	Intuicyjne narzędzie do wypalania CD
Name:		cdbakeoven
Version:	2.0
Release:	0.%{beta}.3
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/%{name}/%{name}-i18n-%{version}%{beta}.tar.bz2
# Source0-md5:	52c2e0af4764f13ede315b1a0373236c
URL:		http://cdbakeoven.sourceforge.net/
BuildRequires:	bzip2
BuildRequires:	kdelibs-devel >= 3.1
Requires:	cdrtools
Requires:	cdrtools-cdda2wav
Requires:	cdrtools-mkisofs
Requires:	cdparanoia-III
Requires:	kdelibs >= 3.1
Requires:	vorbis-tools >= 1.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	kdeutils-%{name}

%define		_htmldir	/usr/share/doc/kde/HTML

%description
CD Bake Oven was designed with one goal in mind: combine the power and
stability of great command line utilities with contemporary easy to
use user interface. CDBO enables you to create data or music CDs in
the most intuitive matter, allowing you to control every aspect of the
process. It is built on top of very well known 'cdrecord', 'mkisofs',
'cdda2wav' and 'cdparanoia' encapsulating most of the options those
utilities provide. This makes creating professional quality media as
easy as making a few mouse clicks.

%description -l pl.UTF-8
CD Bake Oven został zaprojektowany w jednym celu: połączyć
uniwersalność i stabilność doskonałych narzędzi linii poleceń z łatwym
w użyciu interfejsem. CDBO pozwala tworzyć CD z danymi lub muzyką w
najbardziej intuicyjny sposób, pozwalając kontrolować wszystkie
aspekty procesu. Został zbudowany na bazie doskonale znanych programów
,,cdrecord'', ,,mkisofs'', ,,cdda2wav'' oraz ,,cdparanoia'' dając
dostęp do większości ich opcji. Czyni to tworzenie nośników o
profesjonalnej jakości równie łatwym jak klikanie myszką.

%prep
%setup -q -n %{name}-i18n-%{version}%{beta}

%build
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

CXXFLAGS="%{rpmcflags}" CFLAGS="%{rpmcflags}" ./configure \
	--prefix=%{_prefix}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/{Settings/KDE,Utilities/CD-RW}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

ALD=$RPM_BUILD_ROOT%{_applnkdir}
mv -f $ALD/{Settings/[!K]*,Settings/KDE}
mv -f $ALD/Multimedia $ALD/Utilities/CD-RW
echo "[Desktop Entry]\nName=CDBakeOven\nIcon=cdbakeoven" \
	> $ALD/Settings/KDE/CDBakeOven/.directory

%find_lang %{name}
%clean
%{!?_without_clean:rm -rf $RPM_BUILD_ROOT}

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/kde3/*
%{_datadir}/apps/*
%{_datadir}/mimelnk/application/*
%{_datadir}/mimelnk/inode/*
%{_pixmapsdir}/*/*/*/*
%{_applnkdir}/Utilities/CD-RW/*
%{_applnkdir}/Settings/KDE/*
