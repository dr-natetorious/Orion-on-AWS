// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0
import React from 'react';
import { TopNavigation } from '@cloudscape-design/components';
import AppLayout from '@cloudscape-design/components/app-layout';
import Navigation from './components/navigation';
import Breadcrumbs from './components/breadcrumbs';
import Header from '@cloudscape-design/components/header';
import ContentLayout from '@cloudscape-design/components/content-layout';
import Container from '@cloudscape-design/components/container';
import HelpPanel from '@cloudscape-design/components/help-panel';
import PreparedDashboardContent from './components/prepared-dashboard-content';

export default function App() {
  return (
    <>
      <div id="top-nav">
        <TopNavigation
          identity={{
            logo: { src: '/logo.svg', alt: 'Orion On AWS Logo' },
            title: 'Orion on AWS',
            href: '/home/index.html',
          }}
          utilities={[
            // {
            //   type: "button",
            //   text: "Help",
            //   href: "https://example.com/",
            //   external: true,
            //   externalIconAriaLabel: " (opens in a new tab)"
            // },
            {
              type: "button",
              iconName: "notification",
              title: "Notifications",
              ariaLabel: "Notifications (unread)",
              badge: true,
              disableUtilityCollapse: false
            },
            {
              type: "menu-dropdown",
              iconName: "settings",
              ariaLabel: "Settings",
              title: "Settings",
              items: [
                {
                  id: "settings-org",
                  text: "Organizational settings"
                },
                {
                  id: "settings-project",
                  text: "Project settings"
                }
              ]
            },
            {
              type: "menu-dropdown",
              text: "Customer Name",
              description: "email@example.com",
              iconName: "user-profile",
              items: [
                { id: "profile", text: "Profile" },
                { id: "preferences", text: "Preferences" },
                { id: "security", text: "Security" },
                {
                  id: "support-group",
                  text: "Support",
                  items: [
                    {
                      id: "documentation",
                      text: "Documentation",
                      href: "#",
                      external: true,
                      externalIconAriaLabel:
                        " (opens in new tab)"
                    },
                    { id: "support", text: "Support" },
                    {
                      id: "feedback",
                      text: "Feedback",
                      href: "#",
                      external: true,
                      externalIconAriaLabel:
                        " (opens in new tab)"
                    }
                  ]
                },
                { id: "signout", text: "Sign out" }
              ]
            }
          ]}
          i18nStrings={{
            overflowMenuTriggerText: 'More',
            overflowMenuTitleText: 'All',
          }}
        />
      </div>
      <AppLayout
        headerSelector="#top-nav"
        tools={
          <HelpPanel header={<Header variant='h2'>Help</Header>}>
            <Container>
              This is the help instructions for this page.
              <ul>
                <li>Step 1</li>
                <li>Step 2</li>
                <li>Step 3</li>
              </ul>
            </Container>
          </HelpPanel>
        }
        navigation={<Navigation/>}
        breadcrumbs={<Breadcrumbs/>}
        content={
          <ContentLayout header={<Header variant='h1'>Dashboard</Header>}>
            <PreparedDashboardContent />
          </ContentLayout>
        }
        ariaLabels={{
          navigation: 'Navigation drawer',
          navigationClose: 'Close navigation drawer',
          navigationToggle: 'Open navigation drawer',
          notifications: 'Notifications',
          tools: 'Help panel',
          toolsClose: 'Close help panel',
          toolsToggle: 'Open help panel',
        }}
      />
    </>
  );
}