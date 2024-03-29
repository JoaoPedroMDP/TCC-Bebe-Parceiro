import { Routes } from '@angular/router';
import { HomeComponent, MainComponent } from './index';
import { AuthGuard } from '../auth/guards/auth.guard';

export const AdminRouting: Routes = [
  {
    path: 'admin',
    component: MainComponent, 
    children: [
      { path: '', component: HomeComponent, canActivate: [AuthGuard] },
    ],
    canActivate: [AuthGuard], 
    data: { expectedRole: 'admin' }
  },
];