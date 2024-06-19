import { ComponentFixture, TestBed } from '@angular/core/testing';

import { InspectAppointmentComponent } from './inspect-appointment.component';

describe('InspectAppointmentComponent', () => {
  let component: InspectAppointmentComponent;
  let fixture: ComponentFixture<InspectAppointmentComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ InspectAppointmentComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(InspectAppointmentComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
