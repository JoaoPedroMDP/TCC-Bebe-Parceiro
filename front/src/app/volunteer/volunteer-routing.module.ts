import { Routes } from '@angular/router';
import { HomeComponent } from './components/home/home.component';
import { AuthGuard } from '../auth/guards/auth.guard';
import { MainComponent } from './index';

export const VolunteerRouting: Routes = [
  {
    path: 'voluntaria',
    component: MainComponent,
    children: [
      { path: '', component: HomeComponent, canActivate: [AuthGuard] },
    ],
    canActivate: [AuthGuard],
    data: { expectedRole: 'volunteer' }
  },
];
