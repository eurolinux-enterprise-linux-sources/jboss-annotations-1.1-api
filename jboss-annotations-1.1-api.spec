%global namedreltag .20120212git76e1a2
%global namedversion %{version}%{?namedreltag}

Name: jboss-annotations-1.1-api
Version: 1.0.1
Release: 0.5%{namedreltag}%{dist}
Summary: Common Annotations 1.1 API
Group: Development/Libraries
License: CDDL or GPLv2 with exceptions
URL: http://www.jboss.org

# git clone git://github.com/jboss/jboss-annotations-api_spec.git jboss-annotations-1.1-api
# cd jboss-annotations-1.1-api
# git archive --format=tar --prefix=jboss-annotations-1.1-api-1.0.1/ 76e1a2c85e025342710a29cd9dfff109d730a483 | xz > jboss-annotations-1.1-api-1.0.1.20120212git76e1a2.tar.xz
Source0: %{name}-%{namedversion}.tar.xz

BuildRequires: java-devel
BuildRequires: jboss-specs-parent
BuildRequires: jpackage-utils
BuildRequires: maven-local
BuildRequires: maven-compiler-plugin
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin

Requires: jpackage-utils
Requires: java
BuildArch: noarch


%description
This package contains Common Annotations 1.1 API.


%package javadoc
Summary: Javadocs for %{name}
Group: Documentation
Requires: jpackage-utils


%description javadoc	
This package contains the API documentation for %{name}.


%prep
%setup -q -n %{name}-%{version}


%build
mvn-rpmbuild install javadoc:aggregate


%install

# Jar files:
install -d -m 755 %{buildroot}%{_javadir}
install -pm 644 target/jboss-annotations-api_1.1_spec-%{version}-SNAPSHOT.jar %{buildroot}%{_javadir}/%{name}.jar

# POM files:
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

# Javadoc files:
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -rp target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}/.

# Dependencies map:
%add_maven_depmap JPP-%{name}.pom %{name}.jar

%files
%{_javadir}/*
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%doc LICENSE
%doc README


%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE
%doc README


%changelog
* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-0.5.20120212git76e1a2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.0.1-0.4.20120212git76e1a2
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Tue Jul 24 2012 Juan Hernandez <juan.hernandez@redhat.com> - 1.0.1-0.3.20120212git76e1a2
- Added maven-enforcer-plugin build time dependency

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-0.2.20120212git76e1a2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Mar 12 2012 Juan Hernandez <juan.hernandez@redhat.com> 1.0.1-0.1.20120212git76e1a2
- Packaging after license cleanup upstream

* Wed Feb 22 2012 Juan Hernandez <juan.hernandez@redhat.com> 1.0.0-2
- Cleanup of the spec file

* Tue Jan 24 2012 Marek Goldmann <mgoldman@redhat.com> 1.0.0-1
- Initial packaging

