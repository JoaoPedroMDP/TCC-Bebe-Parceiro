import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ListAppointmentComponent } from './list-appointment.component';

describe('ListAppointmentComponent', () => {
  let component: ListAppointmentComponent;
  let fixture: ComponentFixture<ListAppointmentComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ListAppointmentComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ListAppointmentComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
