
Summary:	Intuitive tool for burning CDs
Summary(pl):	Intuicyjne narz�dzie do wypalania CD
Name:		cdbakeoven
Version:	1.8.9
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.sourceforge.net/pub/sourceforge/%{name}/%{name}-%{version}.tar.bz2
URL:		http://%{name}.sourceforge.net/
BuildRequires:	bzip2
BuildRequires:	kdelibs-devel >= 3.0
Requires:	kdelibs >= 3.0
Requires:	cdrtools
Requires:	cdrtools-cdda2wav
Requires:	cdrtools-mkisofs
Requires:	cdparanoia-III
Obsoletes:      kdeutils-%{name}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_fontdir	/usr/share/fonts
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

%description -l pl
CD Bake Oven zosta� zaprojektowany w jednym celu: po��czy�
uniwersalno�� i stabilno�� doskona�ych narz�dzi linii polece� z �atwym
w u�yciu interfejsem. CDBO pozwala tworzy� CD z danymi lub muzyk� w
najbardziej intuicyjny spos�b, pozwalaj�c kontrolowa� wszystkie
aspekty procesu. Zosta� zbudowany na bazie doskonale znanych program�w
,,cdrecord'', ,,mkisofs'', ,,cdda2wav'' oraz ,,cdparanoia'' daj�c
dost�p do wi�kszo�ci ich opcji. Czyni to tworzenie no�nik�w o
profesjonalnej jako�ci r�wnie �atwym jak klikanie myszk�.

%prep
%setup -q

%build
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

CXXFLAGS="%{rpmcflags}" CFLAGS="%{rpmcflags}" ./configure \
	--prefix=%{_prefix}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d \
    $RPM_BUILD_ROOT%{_applnkdir}/{Settings/KDE,Utilities/CD-RW}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

ALD=$RPM_BUILD_ROOT%{_applnkdir}
mv -f $ALD/{Settings/[!K]*,Settings/KDE}
mv -f $ALD/Utilities/{[!C]*,CD-RW}
echo "[Desktop Entry]\nName=CDBakeOven\nIcon=cdbakeoven" \
    > $ALD/Settings/KDE/CDBakeOven/.directory

%clean
%{!?_without_clean:rm -rf $RPM_BUILD_ROOT}

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/kde3/*
%{_datadir}/apps/*
%{_datadir}/mimelnk/application/*
%{_datadir}/mimelnk/inode/*
%{_pixmapsdir}/*/*/*/*
%{_applnkdir}/Utilities/CD-RW/*
%{_applnkdir}/Settings/KDE/*
