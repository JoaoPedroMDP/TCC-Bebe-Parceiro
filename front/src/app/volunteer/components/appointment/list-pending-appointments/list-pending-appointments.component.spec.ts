import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ListPendingAppointmentsComponent } from './list-pending-appointments.component';

describe('ListPendingAppointmentsComponent', () => {
  let component: ListPendingAppointmentsComponent;
  let fixture: ComponentFixture<ListPendingAppointmentsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ListPendingAppointmentsComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ListPendingAppointmentsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
